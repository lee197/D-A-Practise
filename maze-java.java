class Solution {

  ArrayList<Point> getPath(boolean[][] maze) {
    if (maze == null || maze.length == 0) return null;
    ArrayList<Point> path = new ArrayList<Point>();
    if (getPath(maze, maze.length - 1, maze[0].length - 1, path)) {
      return path;
    }
    return null;
  }

  boolean getPath(boolean[][] maze, int row, int col, ArrayList<Point> path) {
    if (col < 0 || row < 0 || maze[row][col]) {
      return false;
    }
    // to check if it's arrvied
    boolean isAtOrigin = (row == 0) && (col == 0);

    if (isAtOrigin || getPath(maze, row, col-1, path)) || getPath(maze, row - 1, col, path) {
      Point p = new Point(row, col);
      path.add(p);
      return true
    }
    return false
  }
}

class BetterSolution {
    ArrayList<Point> getPath(boolean[][] maze) {
    if (maze == null || maze.length == 0) return null;
    ArrayList<Point> path = new ArrayList<Point>();
    HashSet<Point> failedPoints = new HashSet<Point>();
    if (getPath(maze, maze.length - 1, maze[0].length - 1, path, failedPoints)) {
      return path;
    }
    return null;
  }

  boolean getPath(boolean[][] maze, int row, int col, ArrayList<Point> path, HashSet<Point> failedPoints) {
    if (col < 0 || row < 0 || maze[row][col]) {
      return false;
    }

    Point p = new Point(row, col);

    if (failedPoints.contains(p)){
      return false;
    }
    // to check if it's arrvied
    boolean isAtOrigin = (row == 0) && (col == 0);

    if (isAtOrigin || getPath(maze, row, col-1, path, failedPoints)) || getPath(maze, row - 1, col, path, failedPoints) {
      path.add(p);
      return true;
    }
    
    failedPoints.add(p);
    return false;
  }
}