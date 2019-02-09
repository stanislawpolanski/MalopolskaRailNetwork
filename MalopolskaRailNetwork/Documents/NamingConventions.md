#Issues and commits naming convetions
Pattern: [Issue id] [Title]
##Issue id
Issue number contains of issue type then '-' sign and succesive number of the issue of that type. Types can be:
+ DC - Document change
+ BF - Bug fix
+ ER - Enhancement request
example: DC-001 is the first ticket for document change, BF-005 would be a fifth bug to be fixed
##Commit message convention
[Issue id][optional: ":WIP" or ":MR"] [shortdescription]
[optional: ":WIP"] - if the job is in progress, then add ":WIP" (work in progress), example:
DC-001:WIP Created a base file - that's in progress
DC-001 Work done
Merge request (the end of the job in a branch) will be labelled with :MR, like
DC-002:MR Job done
