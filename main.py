from PySide2 import QtWidgets, QtCore
from pymxs import runtime as rt
import os

class MainWindow(QtWidgets.QMainWindow):
    """Main window for the project preview manager."""
    def __init__(self):
        """Initialize the window."""
        super(MainWindow, self).__init__()

        self.setWindowTitle("Project Preview Manager")

        # Create a central widget.
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout.
        self.layout = QtWidgets.QVBoxLayout()
        self.centralWidget().setLayout(self.layout)

        # Setup the UI.
        self.create_widgets()
        self.create_preset_layout()
        self.create_resolution_layout()
        self.create_output_layout()
        self.create_input_groupbox()
        self.create_settings_groupbox()
        self.create_output_groupbox()
        self.add_widgets_to_layout()
        self.adjust_labels()
        self.set_size_policy()
        self.set_button_height()
        self.connect_functions()
        self.disable_widgets()
        
    def create_widgets(self):
        """Create the widgets for the window."""

        # Create a button to select the input directory and a label to display the selected path.
        self.button_input_directory = QtWidgets.QPushButton("Choose directory")
        self.label_input_path = QtWidgets.QLabel("No input path selected")

        # Create a label with instructions to select the preset settings.
        self.label_preset = QtWidgets.QLabel("Select preset: ")

        # Create a combo box for the preset settings.
        self.combobox_preset = QtWidgets.QComboBox()
        self.combobox_preset.addItem("Render active view")
        self.combobox_preset.addItem("Current view screenshot")
        self.combobox_preset.addItem("Screenshots of all views")

        # Create a label with instructions to select the render resolution settings.
        self.label_resolution = QtWidgets.QLabel("Select render resolution: ")  

        # Create a combo box for the render resolution settings.
        self.combobox_resolution = QtWidgets.QComboBox()
        self.combobox_resolution.addItem("100% original resolution")
        self.combobox_resolution.addItem("50% original resolution")
        self.combobox_resolution.addItem("25% original resolution")
        self.combobox_resolution.addItem("10% original resolution")

        # Create a label with instructions to select the output method.
        self.label_output_method = QtWidgets.QLabel("Choose output method: ")

        # Create a combo box for the output settings.
        self.combobox_output = QtWidgets.QComboBox()
        self.combobox_output.addItem("Save to the original directory of the .max file(s)")
        self.combobox_output.addItem("Choose new output directory")

        # Create a button to select the output directory and a label to display the selected path.
        self.button_output_directory = QtWidgets.QPushButton("Choose directory")
        self.label_output_path = QtWidgets.QLabel("No output path selected")

        # Create a button to create the preview.
        self.button_create_preview = QtWidgets.QPushButton("Create Preview")

    def create_preset_layout(self):
        """Create the layout for the preset settings."""
        self.preset_layout = QtWidgets.QHBoxLayout()
        self.preset_layout.addWidget(self.label_preset)
        self.preset_layout.addWidget(self.combobox_preset)
        self.preset_layout.setAlignment(QtCore.Qt.AlignVCenter)

    def create_resolution_layout(self):
        """Create the layout for the resolution settings."""
        self.resolution_layout = QtWidgets.QHBoxLayout()
        self.resolution_layout.addWidget(self.label_resolution)
        self.resolution_layout.addWidget(self.combobox_resolution)
        self.resolution_layout.setAlignment(QtCore.Qt.AlignVCenter)

    def create_output_layout(self):
        """Create the layout for the output settings."""
        self.output_layout = QtWidgets.QHBoxLayout()
        self.output_layout.addWidget(self.label_output_method)
        self.output_layout.addWidget(self.combobox_output)
        self.output_layout.setAlignment(QtCore.Qt.AlignVCenter)

    def create_input_groupbox(self):
        """Setup the input group box and its widgets."""
        self.input_group_box_layout = QtWidgets.QVBoxLayout()
        self.input_group_box_layout.addWidget(self.button_input_directory)
        self.input_group_box_layout.addWidget(self.label_input_path)
        self.input_group_box = QtWidgets.QGroupBox("Input Path")
        self.input_group_box.setLayout(self.input_group_box_layout)

    def create_settings_groupbox(self):
        """Create the settings group box and its widgets."""
        self.settings_group_box_layout = QtWidgets.QVBoxLayout()
        self.settings_group_box_layout.addLayout(self.preset_layout)
        self.settings_group_box_layout.addLayout(self.resolution_layout)
        self.settings_group_box_layout.addLayout(self.output_layout)
        self.settings_group_box = QtWidgets.QGroupBox("Settings")
        self.settings_group_box.setLayout(self.settings_group_box_layout)

    def create_output_groupbox(self):
        """Create the output group box and its widgets."""
        self.output_group_box_layout = QtWidgets.QVBoxLayout()
        self.output_group_box_layout.addWidget(self.button_output_directory)
        self.output_group_box_layout.addWidget(self.label_output_path)
        self.output_group_box = QtWidgets.QGroupBox("Output Path")
        self.output_group_box.setLayout(self.output_group_box_layout)

    def add_widgets_to_layout(self):
        """Add the widgets to the main layout."""
        self.layout.addSpacing(3)  # Add spacing.
        self.layout.addWidget(self.input_group_box)
        self.layout.addSpacing(3)  # Add spacing.
        self.layout.addWidget(self.settings_group_box)
        self.layout.addSpacing(3)  # Add spacing.
        self.layout.addWidget(self.output_group_box)
        self.layout.addSpacing(6)  # Add spacing.
        self.layout.addWidget(self.button_create_preview)
        self.layout.addSpacing(4)  # Add spacing.

    def adjust_labels(self):
        """Adjust the appearance of the labels."""

        # Align to the center.
        self.label_input_path.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_path.setAlignment(QtCore.Qt.AlignCenter)

        # Enable word wrapping.
        self.label_input_path.setWordWrap(True)
        self.label_output_path.setWordWrap(True)

        # Add margins.
        self.label_input_path.setContentsMargins(5, 5, 5, 5)
        self.label_output_path.setContentsMargins(5, 5, 5, 5)

        # Get the size hints for all the settings labels.
        size_hints = [self.label_preset.sizeHint(), self.label_resolution.sizeHint(), self.label_output_method.sizeHint()]

        # Find the maximum width.
        max_width = max(size.width() for size in size_hints)

        # Set all label width to the widest label to have a consistent appearance.
        self.label_preset.setFixedWidth(max_width)
        self.label_resolution.setFixedWidth(max_width)
        self.label_output_method.setFixedWidth(max_width)

    def set_size_policy(self):
        """Set the size policy for the widgets."""

        # Set the size policy for the combo boxes and buttons.
        button_sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_input_directory.setSizePolicy(button_sizePolicy)
        self.combobox_preset.setSizePolicy(button_sizePolicy)
        self.combobox_resolution.setSizePolicy(button_sizePolicy)
        self.button_output_directory.setSizePolicy(button_sizePolicy)  
        self.combobox_output.setSizePolicy(button_sizePolicy)
        self.button_create_preview.setSizePolicy(button_sizePolicy)

        # Set the size policy for the input/output path labels.
        label_sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.label_input_path.setSizePolicy(label_sizePolicy)
        self.label_output_path.setSizePolicy(label_sizePolicy)

    def set_button_height(self):
        """Set the minimum height for the buttons."""
        self.button_input_directory.setMinimumHeight(35)
        self.button_output_directory.setMinimumHeight(35)
        self.button_create_preview.setMinimumHeight(45)

    def connect_functions(self):
        """Connect the widgets to their respective methods."""
        self.button_input_directory.clicked.connect(self.choose_input_directory)
        self.button_output_directory.clicked.connect(self.choose_output_directory)
        self.button_create_preview.clicked.connect(self.create_preview)

        # Connect the combo boxes' currentIndexChanged signals to the check_conditions method.
        self.combobox_preset.currentIndexChanged.connect(self.check_conditions)
        self.combobox_output.currentIndexChanged.connect(self.check_conditions)

    def disable_widgets(self):
        """Disable the widgets initially."""
        self.label_input_path.setEnabled(False)
        self.label_output_path.setEnabled(False)
        self.settings_group_box.setEnabled(False)
        self.output_group_box.setEnabled(False)
        self.button_create_preview.setEnabled(False)

    def choose_input_directory(self):
        """Open a dialog to select the input directory and display the path in the label."""
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory")
        if directory:
            self.label_input_path.setText("Selected input path: " + directory)
            # Check if conditions are met to enable the widgets.
            self.check_conditions()

    def choose_output_directory(self):
        """Open a dialog to select the output directory and display the path in the label."""
        output_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose directory")
        if output_path:
            self.label_output_path.setText("Selected output path: " + output_path)
            # Check if conditions are met to enable the widgets.
            self.check_conditions()

    def check_conditions(self):
        """Check if the conditions are met to enable the widgets."""

        # Enable the widgets when a directory is selected.
        if self.label_input_path.text() != "No directory selected":
            self.label_input_path.setEnabled(True)
            self.settings_group_box.setEnabled(True)

        # Enable the output path label when an output path is selected.
        if self.label_output_path.text() != "No output path selected":
            self.label_output_path.setEnabled(True)
        else:
            self.label_output_path.setEnabled(False)

        # Enable output_group_box when an input directory is chosen and the "Choose new output directory" option is selected.
        if self.label_input_path.text() != "No directory selected" and self.combobox_output.currentText() == "Choose new output directory":
            self.output_group_box.setEnabled(True)
        else:
            self.output_group_box.setEnabled(False)

        # Enable or disable the resolution options based on the selected preset.
        if self.combobox_preset.currentText() == "Render active view":
            self.label_resolution.setEnabled(True)
            self.combobox_resolution.setEnabled(True)
        else:
            self.label_resolution.setEnabled(False)
            self.combobox_resolution.setEnabled(False)

        # Enable the "Create Preview" button if:
        # 1) an input directory is selected and combobox_output option is set to "Save to the original directory of the .max file(s)".
        # 2) an input directory is selected, combobox_output option is set to "Choose new output directory" and a new output path is selected.
        if self.label_input_path.text() != "No directory selected" and (
            (self.combobox_output.currentText() == "Save to the original directory of the .max file(s)") or
            (self.combobox_output.currentText() == "Choose new output directory" and self.label_output_path.text() != "No output path selected")
        ):
            self.button_create_preview.setEnabled(True)
        else:
            self.button_create_preview.setEnabled(False)

    def construct_path(self):
        """Construct the path for the preview images based on the current settings."""

        # Get the path of the currently open max file.
        max_file_path = os.path.normpath(rt.maxFilePath + rt.maxFileName)

        # Get the base name of the max file (without the extension).
        base_name = os.path.splitext(os.path.basename(max_file_path))[0]

        # Determine the current preset.
        preset_setting = self.combobox_preset.currentText()

        # Add the appropriate suffix based on the preset.
        if preset_setting == "Render active view":
            suffix = "_preview_render.png"
        elif preset_setting == "Current view screenshot":
            suffix = "_screenshot.png"
        else:
            suffix = ""

        # Construct the new file name.
        new_file_name = f"{base_name}{suffix}"

        # Determine the output directory.
        if self.combobox_output.currentText() == "Choose new output directory":
            output_directory = os.path.normpath(self.label_output_path.text().replace("Selected output path: ", ""))
        else:
            output_directory = os.path.normpath(os.path.dirname(max_file_path))

        # Construct the full path to the new file.
        new_file_path = os.path.normpath(os.path.join(output_directory, new_file_name))

        return new_file_path

    def create_renders(self):
        """Create renders for all .max files in the chosen directory."""

        # Get the chosen directory from the label.
        directory = self.label_input_path.text().replace("Selected input path: ", "")
        
        # Get all .max files in the directory and its subdirectories.
        max_files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            max_files.extend([os.path.join(dirpath, f) for f in filenames if f.endswith('.max')])
        
        # Loop over the .max files.
        for max_file in max_files:

            # Open the .max file.
            rt.loadMaxFile(max_file)

            # Construct the new file path.
            new_file_path = self.construct_path()

            # Set the render resolution according to the settings and perform a quick render. Save the render to the new file path.
            resolution_setting = self.combobox_resolution.currentText()
            original_width = rt.renderWidth
            original_height = rt.renderHeight

            if resolution_setting == "100% original resolution":
                rt.renderWidth = original_width
                rt.renderHeight = original_height
            elif resolution_setting == "50% original resolution":
                rt.renderWidth = int(original_width * 0.5)
                rt.renderHeight = int(original_height * 0.5)
            elif resolution_setting == "25% original resolution":
                rt.renderWidth = int(original_width * 0.25)
                rt.renderHeight = int(original_height * 0.25)
            elif resolution_setting == "10% original resolution":
                rt.renderWidth = int(original_width * 0.1)
                rt.renderHeight = int(original_height * 0.1)

            maxscript_code = f"""
            rendSaveFile = true
            rendOutputFilename = "{new_file_path}"
            rendTimeType = 1  -- Set the time output to single frame.
            max quick render
            """
            rt.execute(maxscript_code)

    def create_single_screenshot(self):
        """Create a screenshot of the current active view for all .max files in the chosen directory."""

        # Get the chosen directory from the label.
        directory = self.label_input_path.text().replace("Selected input path: ", "")
        
        # Get all .max files in the directory and its subdirectories.
        max_files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            max_files.extend([os.path.join(dirpath, f) for f in filenames if f.endswith('.max')])
        
        # Loop over the .max files.
        for max_file in max_files:

            # Open the .max file.
            rt.loadMaxFile(max_file)

            # Construct the new file path.
            new_file_path = self.construct_path()

            # Create a screenshot of the current active view and save it to the new file path.
            maxscript_code = f"""
            img = gw.getViewportDib()
            img.filename = "{new_file_path}"
            save img
            """
            rt.execute(maxscript_code)

    def create_multiple_screenshots(self):
        """Create screenshots of all views for all .max files in the chosen directory."""

        # Get the chosen directory from the label.
        directory = self.label_input_path.text().replace("Selected input path: ", "")
        
        # Get all .max files in the directory and its subdirectories.
        max_files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            max_files.extend([os.path.join(dirpath, f) for f in filenames if f.endswith('.max')])
        
        # Define the views.
        views = ["view_iso_user", "view_persp_user", "view_front", "view_left", "view_right", "view_back", "view_top", "view_bottom"]
        
        # Loop over the .max files.
        for max_file in max_files:

            # Open the .max file.
            rt.loadMaxFile(max_file)

            # Construct the new file path.
            new_file_path = self.construct_path()

            # Create a screenshot of the current active view and save it to the new file path.
            maxscript_code = f"""
            img = gw.getViewportDib()
            img.filename = "{new_file_path}_active_view.png"
            save img
            """
            rt.execute(maxscript_code)

            # Create a screenshot of each of the defined views and save it to the new file path.
            for view in views:
                maxscript_code = f"""
                viewport.setType #{view}
                actionMan.executeAction 0 "331"  -- Zoom extents all.
                img = gw.getViewportDib()
                img.filename = "{new_file_path}_{view}.png"
                save img
                """
                rt.execute(maxscript_code)

    def create_preview(self):
        """Create the preview based on the current settings."""

        # Determine the current settings.
        preset_setting = self.combobox_preset.currentText()

        # Execute the appropriate action based on the settings.
        if preset_setting == "Render active view":
            self.create_renders()
        elif preset_setting == "Current view screenshot":
            self.create_single_screenshot()
        else:
            self.create_multiple_screenshots()

# Create and show the window.
app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication([])
window = MainWindow()
window.resize(300, 200)  # Set the window size to 300x200 pixels.
window.show()