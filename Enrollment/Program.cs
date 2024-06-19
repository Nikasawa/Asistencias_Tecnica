using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Windows.Forms;

namespace Enrollment
{
	static class Program
	{
		/// <summary>
		/// The main entry point for the application.
		/// </summary>
 
		[STAThread]
		static void Main()
		{
            // Intento de conexion a la base de datos
            string connectionString = "server=localhost;" +
                                      "database=asistencias;" +
                                      "user=root;";

            using (MySqlConnection conn = new MySqlConnection(connectionString))
            {
                try
                {
                    conn.Open();
                    Console.WriteLine("Connection successful!");

                    // Ejemplo de una consulta SELECT
                    string query = "SELECT * FROM your_table";
                    MySqlCommand cmd = new MySqlCommand(query, conn);

                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Debug.WriteLine(reader["column_name"]);
                        }
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error: {ex.Message}");
                }
            }
            Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);
			Application.Run(new MainForm());
		}
	}
}