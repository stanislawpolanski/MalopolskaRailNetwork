import src.Files.FilesLister
import src.Constants.ProjectPaths

mainDirectoryPath = src.Constants.ProjectPaths.ProjectPathsStore.XMLSourceDataFolder.value
src.Files.FilesLister.FilesLister(mainDirectoryPath)

for path in src.Files.FilesLister.filesPathsList:
    print(path)