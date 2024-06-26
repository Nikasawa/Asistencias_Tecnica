using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Pruebas_mas_nashe
{
    internal class Conexion
    {
        private string server = "localhost";
        private string database = "asistencias";
        private string user = "root";
        private string password = "";
        private string cadenaConexion;
        private MySqlConnection conexion;

        public Conexion()
        {
            cadenaConexion = "Database=" + database +
                             "; DataSource=" + server +
                             "; User Id=" + user +
                             "; Password=" + password;
           
        }

        public MySqlConnection getConexion() {

            if (conexion == null)
            {
                conexion = new MySqlConnection(cadenaConexion);
                conexion.Open();
            }
                return conexion;
            
        }
    }
}
