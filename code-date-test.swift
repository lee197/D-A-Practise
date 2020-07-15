import Foundation

//Networking
enum APIError: String, Error {
    case clientError
    case serverError
    case emptyData
    case dataDecodingError
}

class NetworkingService {
    var apiKey = "72cc8e7efb7a890488cd1eb7dbfa"
    var urlComponents = URLComponents()
    
    init() {
        urlComponents.scheme = "https"
        urlComponents.host = "candidate.hubteam.com"
        urlComponents.queryItems = [
            URLQueryItem(name: "userKey", value: apiKey),
        ]
    }
    
    func fetchData(completionHandler completion: @escaping (Result<Partners, APIError>)->(Void)) {
        urlComponents.path = "/candidateTest/v3/problem/dataset"
        
        var request: URLRequest {
            let request = URLRequest(url: urlComponents.url!,cachePolicy: .reloadIgnoringLocalCacheData)
            return request
        }
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let _ = error {
                completion(.failure(.clientError))
                return
            }
            
            guard let response = response as? HTTPURLResponse, 200...299 ~= response.statusCode else {
                completion(.failure(.serverError))
                return
            }
            
            guard let data = data else {
                completion(.failure(.emptyData))
                return
            }
            
            let decoder = JSONDecoder()
            do{
                let value = try decoder.decode(Partners.self, from: data)
                completion(.success(value))
            }catch{
                completion(.failure(.dataDecodingError))
            }
        }.resume()
    }
    
    func postResult(with data:Data) {
        urlComponents.path = "/candidateTest/v3/problem/result"
        
        var request: URLRequest {
            var request = URLRequest(url: urlComponents.url!,cachePolicy: .reloadIgnoringLocalCacheData)
            request.httpMethod = "POST"
            request.setValue("Application/json", forHTTPHeaderField: "Content-Type")
            request.httpBody = data
            return request
        }
        
        URLSession.shared.dataTask(with: request) { (data, response, error) in
            if let response = response {
                print(response)
            }
            if let data = data {
                do {
                    let _ = try JSONSerialization.jsonObject(with: data, options: [])
                    
                } catch {
                    print(error)
                }
            }
        }.resume()
    }
}

// Model
struct Partners: Decodable {
    let partners: [Partner]
}

struct Partner: Decodable {
    let email: String
    let country: String
    var availableDates: [String]
    var availableDatePairs: [DatePair] {
        
        let dates = availableDates.map { dateStr in
            DataFormatter.shared().date(from: dateStr)
        }.compactMap { $0 }
        
        if dates.count < 2 {
            return []
        }
        
        var datePairs = [DatePair]()
        for index in 1...dates.count-1 {
            if dates[index].distance(from: dates[index-1], resultIn: .day) == -1 {
                let datePair = DatePair(firstDay: dates[index-1], secondDay: dates[index])
                datePairs.append(datePair)
            }
        }
        
        return datePairs
    }
}

struct DatePair: Comparable, Hashable {
    
    let firstDay: Date
    let secondDay: Date
    
    static func < (lhs: DatePair, rhs: DatePair) -> Bool {
        return lhs.firstDay < rhs.firstDay
    }
}

struct Results: Encodable {
    let countries: [Country]
}

struct Country: Encodable {
    var attendeeCount: Int {
        return attendees.count
    }
    var attendees: [String]
    let name: String
    var startDate: String? {
        if let pairedStartDate = pairedStartDate {
            return DataFormatter.shared().string(from: pairedStartDate.firstDay)
        } else {
            return nil
        }
    }
    var pairedStartDate: DatePair?
    
    private enum CodingKeys: String, CodingKey {
        case attendeeCount, attendees, name, startDate
    }
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode (attendeeCount, forKey: .attendeeCount)
        try container.encode (attendees, forKey: .attendees)
        try container.encode (name, forKey: .name)
        try container.encode (startDate, forKey: .startDate)
    }
}

// Support classes
extension Date {
    
    func distance(from date: Date, resultIn component: Calendar.Component, calendar: Calendar = .current) -> Int? {
        return calendar.dateComponents([component], from: self, to: date).value(for: component)
    }
}

class DataFormatter {
    private static var dateFormatter: DateFormatter {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd"
        dateFormatter.timeZone = TimeZone(abbreviation: "UTC")
        return dateFormatter
    }
    class func shared() -> DateFormatter {
        return dateFormatter
    }
}

// ViewModel
struct PartenerViewModel {
    private var networkingService: NetworkingService
    
    init(networkingService: NetworkingService = NetworkingService()) {
        self.networkingService = networkingService
    }
    
    func initFetch() {
        networkingService.fetchData { result in
            
            switch result {
            case .success(let partners):
                self.processData(partners: partners.partners)
            case .failure(let error):
                self.processError(error: error)
            }
        }
    }
    
    func submitResult(coutriesWithPartners: [Country]) {
        do {
            let result = Results(countries: coutriesWithPartners)
            let data = try JSONEncoder().encode(result)
            let string = String(data: data, encoding: .utf8)!
            print(string)
            self.networkingService.postResult(with: data)
        } catch let error {
            print(error)
        }
    }
    
    private func processData(partners: [Partner]) {
        let countryDict = createCountryDict(with: partners)
        let countryList = convertToCountryModels(with: countryDict)
        let coutriesWithPartners = findTargetPartners(with: countryList, and: partners)
        submitResult(coutriesWithPartners: coutriesWithPartners)
    }
    
    private func createCountryDict(with partners: [Partner]) -> [String:[DatePair]] {
        var result = [String:[DatePair]]()
        partners.forEach { partner in
            if result[partner.country] == nil {
                result[partner.country] = [DatePair]()
                result[partner.country]?.append(contentsOf: partner.availableDatePairs)
            } else {
                result[partner.country]?.append(contentsOf: partner.availableDatePairs)
            }
        }
        
        return result
    }
    
    private func convertToCountryModels(with countryDict: [String:[DatePair]]) -> [Country] {
        let countryList = countryDict.map { val -> Country in
            var country = Country(attendees: [], name: val.key, pairedStartDate: nil)
            let pair = val.value
            if pair.count != 0 {
                country.pairedStartDate = findMostFrequentDatePair(from: pair)
            }
            
            return country
        }
        
        return countryList
    }
    
    private func findTargetPartners( with countryList: [Country], and partners: [Partner] ) -> [Country] {
        var countries = countryList
        for index in 0...countries.count-1 {
            for partner in partners {
                if partner.country == countries[index].name && partner.availableDatePairs.contains(where: { $0 == countries[index].pairedStartDate! }) {
                    countries[index].attendees.append(partner.email)
                }
            }
        }
        return countries
    }
    
    private func findMostFrequentDatePair(from dateArray: [DatePair]) -> DatePair {
        let mappedItems = dateArray.map { ($0, 1) }
        let frequency = Dictionary(mappedItems, uniquingKeysWith: +).max(by: { val1, val2 in
            if val1.value == val2.value {
                return val1.key > val2.key
            }else{
                return val1.value < val2.value
            }
        })
        return frequency!.key
    }
    
    private func processError(error: APIError) {
        print(error)
    }
}

// View
var partnerViewModel = PartenerViewModel()
partnerViewModel.initFetch()
