import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(426, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter The Number of Calories in Food"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 50)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(453, 41)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter The Number of Fat Grams in Food"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(469, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Percentage of Calories that come from Fat"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(456, 18)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(160, 20)
        self._textBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(674, 290)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog268"
        self.ResumeLayout(False)
        self.PerformLayout()

