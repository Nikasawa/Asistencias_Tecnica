using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace UI_Support {
  static class Program {
    /// <summary>
    /// The main entry point for the application.
    /// </summary>
    [STAThread]
    static void Main() {
      Application.EnableVisualStyles();
      Application.SetCompatibleTextRenderingDefault(false);
      Application.Run(new MainForm());

            
            conexion.getConexion();

            string consulta = "SELECT NOW()";

            using (MySqlCommand comando = new MySqlCommand(consulta, conexion))
            {
                object result = comando.ExecuteReader();

                if (result != null)
                {
                    DateTime hora = Convert.ToDateTime(result);
                    Console.WriteLine(hora.ToString("HH:mm:ss"));
                }
            }
        
    }
        Conexion conexion = new Conexion();
   }
}