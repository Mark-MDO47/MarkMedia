# MarkMedia
annotate my pictures and videos

# use wxFormBuilder to make (so far) Python media explorer
The script combine.sh adds my changes (events, merges, etc.) to wxFormBuilder input.
This allows me to iterate on both wxFormBuilder and on my additions.

Just getting started; hardly anything is hooked to an event and they don't do the real things yet.

# Flow
Flow is as follows:
- use wxFormBuilder in ./wxFormBuilder_MarkMedia/ to build the look of the app
- export as Python 3.x code in ./wxFormBuilder_MarkMedia/
- run ./PyMarkMedia/combine.sh in ./PyMarkMedia/ to insert my event handlers
- do python MarkMedia.py in ./PyMarkMedia/ to execute the resulting test code
  - use File->OpenVideoTxt and open free-form descriptive text for videos

![alt text](https://github.com/Mark-MDO47/MarkMedia/blob/master/PyMarkMedia.png "MarkMedia in action")

At some point it will be easier just to make a dialog using wxFormBuilder and hand-edit into the codebase
