Python script for 3ds Max with a user interface to create preview renders and screenshots of .max files in batch.

The purpose of the script is to create preview renders or screenshots of all 3ds Max files in the directory
chosen by the user including its subfolders. Once an input directory is selected it will be displayed in the
input path label and the settings options will be enabled:

a) Select Preset:
	1) "Render active view" - renders the active view of each of the 3ds Max files.
	2) "Current view screenshot" - makes a screenshot of the current active view.
	3) "Screenshots of all views" - makes screenshots of all views (orthographic, perspective, front, back,
	left, right, top and bottom.

b) Select render resolution(this options will only be enabled if the "Render active view" option is selected):
	1) "100% original resolution" - makes the render of the active view in the original resolution set in the
	3ds Max file.
	2) "50% original resolution" - makes the render of the active view at 50% of the resolution set in the 3ds
	Max file.
	3) "25% original resolution" - makes the render of the active view at 25% of the resolution set in the 3ds
	Max file.
	4) "10% original resolution" - makes the render of the active view at 10% of the resolution set in the 3ds
	Max file.

c) Choose output method:
	1) "Save to the original directory of the .max file(s)" - saves the previews in the original directory of
	each of the 3ds Max files.
	2) "Choose new output directory" - saves the previews in a new directory selected by the user. Selecting
	this option enables the button to choose the new output path.

Once the necessary options are selected by the user the "Create Preview" button is enabled to create the preview
images.
	