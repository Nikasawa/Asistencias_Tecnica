using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pruebas_mas_nashe
{
    public partial class Form1 : Form
    {
        private Conexion mConexion;

        public Form1()
        {
            InitializeComponent();
            
            mConexion = new Conexion();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            MySqlDataReader mySqlDataReader = null;
            string consulta = "select * from prueba";

            if (mConexion != null)
            {
                MySqlCommand mySqlCommand = new MySqlCommand(consulta);
                mySqlCommand.Connection = mConexion.getConexion();
                mySqlDataReader = mySqlCommand.ExecuteReader();


                while (mySqlDataReader.Read())
                {
                    if (!mySqlDataReader.IsDBNull(0))
                    {
                        try
                        {
                            DateTime result = mySqlDataReader.GetMySqlDateTime("fecha");
                            label2.Text = result.ToString("yyyy-MM-dd");
                        }
                        catch (MySql.Data.Types.MySqlConversionException ex)
                        {
                            // Manejar la excepción de conversión de fecha/hora
                            MessageBox.Show($"Error converting date: {ex.Message}");
                        }
                    }
                    else
                    {
                        // Manejar el caso donde el valor es NULL
                        label2.Text = "Fecha nula";
                    }
                }

                

            } else
            {
                MessageBox.Show("Error de conexion");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
