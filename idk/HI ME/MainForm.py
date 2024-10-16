import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(395, 189)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(174, 83)
        self._button1.TabIndex = 0
        self._button1.Text = "START"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(395, 319)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(174, 83)
        self._button2.TabIndex = 1
        self._button2.Text = "EXIT"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(395, 63)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(174, 76)
        self._label1.TabIndex = 2
        self._label1.Text = "HI ME"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.OrangeRed
        self.ClientSize = System.Drawing.Size(1009, 440)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "HI ME"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        self._label1.Text = "HI ME"
        
    def Button2Click(self, sender, e):
        Application.Exit()
        