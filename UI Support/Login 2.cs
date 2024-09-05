using MySql.Data.MySqlClient;

namespace UI_Support
{
    partial class login
    {
        private login()
        {
            conexion.getConexion();
        }

        // Los parametros de entrada de la funcion login son los que ingrese el usuario en las cajas de texto
        private string crearCuenta(string adm_Nombre, string adm_Apellido, string adm_DNI, string Usuario_Contraseña, string Usuario_Correo)
        {
            string consulta = '';
            MySqlCommand comando = null;
            MySqlDataReader resultado = null;

            // Revisar si el correo ya existe
            consulta = "SELECT * FROM adm WHERE Usuario_Correo = @Usuario_Correo";
            using (comando = MySQLCommand(consulta, conexion))
            {
                comando.AddWithValue("@Usuario_Correo", Usuario_Correo);
                resultado = comando.ExecuteReader()



            if (resultado.Read())
                {
                    return "El correo o contraseña ya existe";
                }

            }

            // Revisar si la contraseña ya existe
            consulta = "SELECT * FROM adm WHERE Usuario_Contraseña = @Usuario_Contraseña";
            using (comando = MySQLCommand(consulta, conexion))
            {
                comando.AddWithValue("@Usuario_Contraseña", Usuario_Contraseña);
                resultado = comando.ExecuteReader()



            if (resultado.Read())
                {
                    return "El correo o contraseña ya existe";
                }
            }

            // En caso de que no se haya registrado previamente se toman los datos ingresados y se hace un insert en la tabla
            consulta = "INSERT INTO adm (adm_Nombre, adm_Apellido, adm_DNI, Usuario_Contraseña, Usuario_Correo) VALUES (@adm_Nombre, @adm_Apellido, @adm_DNI, @Usuario_Contraseña, @Usuario_Correo)";
            using (comando = new MySQLCommand(consulta, conexion))
            {
                comando.Parameters.AddWithValue("@adm_Nombre", adm_Nombre);
                comando.Parameters.AddWithValue("@adm_Apellido", adm_Apellido);
                comando.Parameters.AddWithValue("@adm_DNI", adm_DNI);
                comando.Parameters.AddWithValue("@Usuario_Contraseña", Usuario_Contraseña);
                comando.Parameters.AddWithValue("@Usuario_Correo", Usuario_Correo);
                comando.ExecuteReader();

                return "El usuario se registro con exito";
            }
        }

        private string loginUsuario(string Usuario_Correo, string Usuario_Contraseña)
        {
            string consulta = '';
            MySqlCommand comando = null;
            MySqlDataReader resultado = null;

            // Busca un registro en la tabla que coincida con el correo y la contraseña que se ingreso.
            // No hay mensaje de error, solo una devolucion del nombre y apellido en caso de que se haya encontrado un usuario con el correo y contraseña
            consulta = "SELECT * FROM adm WHERE Usuario_Correo = @Usuario_Correo AND Usuario_Contraseña = @Usuario_Contraseña";
            using (command = new MySqlCommand(consulta, conexion))
            {
                commando.AddWithValue("@Usuario_Correo", Usuario_Correo);
                commando.AddWithValue("@Usuario_Contraseña", Usuario_Contraseña);
                resultado = comando.ExecuteReader();

                if (resultado.Read)
                {
                    string adm_Nombre = resultado.GetString("adm_Nombre");
                    string adm_Apellido = resultado.GetString("adm_Apellido");

                    // Devuelve un array con los atributos
                    string[2] atributosUsuario = [adm_Nombre, adm_Apellido];

                    return atributosUsuario;
                }

            }
        }
        void DarDeBaja(string tabla, int ID)
        {

            string consulta = '';
            MySqlCommand comando = null;

            // Recupera todo la informacion de la persona seleccionada
            consulta = $"SELECT * FROM adm WHERE ID = " + ID.ToString();

            string Nombre;
            string Apellido;

            using (comando = new MySqlCommand(consulta, conexion))
            {
                MySqlDataReader result = comando.ExecuteReader();

                if (result.Read())
                {
                    // De momento solo se toma el nombre y el apellido porque no sabemos que debe tener realmente la tabla de bajas
                    Nombre = result.GetString("Nombre");
                    Apellido = result.GetString("Apellido");
                }
            }

            // Enviarlo a la tabla de bajas
            consulta = $"INSERT (Nombre, Apellido) INTO " + tabla + " VALUES (@Nombre, @Apellido)";

            using (comando = new MySqlCommand(consulta, conexion))
            {
                comando.Parameters.AddWithValue("@Nombre", Nombre);
                comando.Parameters.AddWithValue("@Apellido", Apellido);
                comando.ExecuteReader();
            }

            // Elimina de la tabla seleccionada 
            consulta = $"DELETE FROM " + tabla + " WHERE ID = " + ID.ToString();

            using (comando = new MySqlCommand(consulta, conexion))
            {
                comando.ExecuteReader();
            }

        }


    }

    private Conexion conexion = new Conexion();

}