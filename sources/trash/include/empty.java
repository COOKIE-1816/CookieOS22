package cookieos_trash_empty;

import java.util.*;
import java.io.File.*;
import java.io.IOException;
import java.nio.file.*;

public class Trash_Empty {
    Path path = "x:/cos-trash"
    public boolean isEmpty(Path path) throws IOException {
        if(Files.isDirectory(path)) {
            try(DirectoryStream<Path> directory = Files.newDirectoryStream(path)) {
                return !directory.iterator.hasNext();
            }
        }

        return false;
    }

    public static void Main(String args[]) {
        if(Trash_Empty.isEmpty(Trash_Empty.path)) {
            System.out.print("Trash is empty already.");
        } else {
            List<String> fileNames = new ArrayList<>();

            try {
                DirectoryStream<Path> DirectoryStream = Files.newDirectoryStream(Paths.get(Trash_Empty.path));

                for(Path path: directoryStream) {
                    fileNames.add(path.toString());
                }
            } catch(IOException ex) {}

            String file_count = fileNames.size();


            System.out.print("\nAre you sure to permanently delete " + file_count + " files from trash? (Y/n)");
            Scanner sc = new Scanner();
            sc_ = sc.nextLine().toLowerCase();

            if(sc_.split("")[0].equals("y")) {
                File directory_ = new File(Trash_Empty.path.toString());
                FileUtils.cleanDirectory(directory_);

                return true;
            }

            System.out.print("\nFile operation aborted.");
            return false;
        }
    }
}