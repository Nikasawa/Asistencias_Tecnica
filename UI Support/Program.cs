using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace UI_Support {

  static class Program {

    /// <summary>
    /// The main entry point for the application.
    /// </summary>
    /// 
    [STAThread]
    static void Main() {
      Console.WriteLine("Hola Cracks De La Informatica!");
            Console.WriteLine("Viva la pepa!");
            Application.EnableVisualStyles();
      Application.SetCompatibleTextRenderingDefault(false);
      Application.Run(new MainForm());
    }
  }
}