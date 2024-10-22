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
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(42, 358)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(180, 75)
        self._button1.TabIndex = 0
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(386, 358)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(180, 75)
        self._button2.TabIndex = 1
        self._button2.Text = "Show"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(711, 358)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(180, 75)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(75, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(816, 282)
        self._label1.TabIndex = 3
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(943, 457)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "About ME"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = ""
        
        

    def Button2Click(self, sender, e):
        self._label1.Text = "My name is Cody and I like to play video games in my freetime"

    def Button3Click(self, sender, e):
        Application.Exit()