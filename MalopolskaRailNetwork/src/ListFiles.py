import src.Files.FilesLister
import src.Constants.ProjectPaths

mainDirectoryPath = src.Constants.ProjectPaths.ProjectPathsStore.Main.value
src.Files.FilesLister.FilesLister(mainDirectoryPath)

for path in src.Files.FilesLister.filesPathsList:
    print(path)