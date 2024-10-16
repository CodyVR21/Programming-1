import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(575, 457)
        self.Name = "MainForm"
        self.Text = "Program52a"
        self.ResumeLayout(False)

