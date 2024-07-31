using DPFP;
using MySql.Data.MySqlClient;
using System;
using System.IO;
using System.Runtime.ConstrainedExecution;
using System.Windows.Forms;

namespace UI_Support
{
    public partial class VerificationForm : Form {
    public VerificationForm(AppData data) {
      InitializeComponent();
      Data = data;
      conexion.getConexion();
        }

    public void OnComplete(object Control, DPFP.FeatureSet FeatureSet, ref DPFP.Gui.EventHandlerStatus Status) {
      DPFP.Verification.Verification ver = new DPFP.Verification.Verification();
      DPFP.Verification.Verification.Result res = new DPFP.Verification.Verification.Result();


            //string consulta = "INSERT INTO pruebahuella ('Nombre', 'Huella1') VALUES ('PollaBulrich', {0})";
            //string consulta = "SELECT * FROM" ;
            // sigo cuando me agarre un pedo


            // Hace un loop revisando cada huella almacenada en "Data"
            //foreach (DPFP.Template template in Data.Templates) {


            //DPFP.Template template = new DPFP.Template();
            //consultarHuellas("pruebahuella", "Huella1", FeatureSet.Bytes);

            // Get template from storage.
            if (true) { // Si la huella no es un valor nulo:


                string tabla = "pruebahuella";
                string consulta = $"SELECT * FROM " + tabla;

                // Compare feature set with particular template.
                using (MySqlCommand comando = new MySqlCommand(consulta, conexion.getConexion()))
                {

                    //comando.Parameters.AddWithValue("@Huella1", huella);

                    using (MySqlDataReader result = comando.ExecuteReader())
                    {
                        

                        byte[] fingerprintData;
                        

                        while (result.Read())
                        {
                            // Console.WriteLine(result.GetByte("Huella1"));
                            // GetBytes(Numero que corresponde a la columna que almacena la huella (Contando a partir del 0),
                            // Ni idea,
                            // cantidad de bytes esperados por fila,
                            // Ni idea,
                            // cantidad de bytes esperados por columna)

                            long length = result.GetBytes(2, 0, null, 0, 0); // Obtener el tama�o del BLOB
                            fingerprintData = new byte[length];
                            result.GetBytes(2, 0, fingerprintData, 0, (int)length); // Leer el BLOB

                            using (MemoryStream memoryStream = new MemoryStream(fingerprintData))
                            {

                                DPFP.Template template = new DPFP.Template(memoryStream);
                                ver.Verify(FeatureSet, template, ref res); // Funcion que compara la huella (creo). �Que es FeatureSet y res?
                                Data.IsFeatureSetMatched = res.Verified; // Bool resultante de la funcion ".Verify". Dicta si la huella coincide o no (boeee "dicta")
                                Data.FalseAcceptRate = res.FARAchieved; // Que es FARAchived?
                                
                            }

                            if (res.Verified)
                            {

                                Console.WriteLine(result.GetString("Nombre"));
                                break;
                            }


                        }
                    }


                }
            }

      // Si la huella que se esta ingresando no coincide con ninguna que este almacenada se envia un mensaje de error
      if (!res.Verified)
        Status = DPFP.Gui.EventHandlerStatus.Failure;

      Data.Update();

    }
        /*
        void consultarHuellas(string tabla, string value, byte[] huella)
        {
            // Revisa que la conexion exista antes de hacer cualquier cosa
            if (conexion.getConexion() == null)
            {
                Console.WriteLine("No se conecto a la base de datos");

                return;

            }

            // Prepara la consulta para la BD, reemplazando "value" y "tabla" con los parametros de entrada
            // string consulta = $"SELECT * FROM " + tabla + " WHERE Huella1 = @Huella1";

            //byte[] fingerprintData;

            // Aplica la consulta a la BD y deja en una variable los resultados que devuelva dicha consulta
            using (MySqlCommand comando = new MySqlCommand(consulta, conexion.getConexion())){

                comando.Parameters.AddWithValue("@Huella1", huella);

                using (MySqlDataReader result = comando.ExecuteReader())
                {
                    Console.WriteLine(comando);

                    while (result.Read())
                    {
                        //Console.WriteLine(result.GetByte("Huella1"));
                        long length = result.GetBytes(0, 0, null, 0, 0); // Obtener el tama�o del BLOB
                        fingerprintData = new byte[length];
                        result.GetBytes(0, 0, fingerprintData, 0, (int)length); // Leer el BLOB

                        ver.Verify(FeatureSet, template, ref res); // Funcion que compara la huella (creo). �Que es FeatureSet y res?
                        Data.IsFeatureSetMatched = res.Verified; // Bool resultante de la funcion ".Verify". Dicta si la huella coincide o no (boeee "dicta")
                        Data.FalseAcceptRate = res.FARAchieved; // Que es FARAchived?

                        //Console.WriteLine("FeatureSet");
                        //Console.WriteLine(FeatureSet);
                        //Console.WriteLine("res");
                        //Console.WriteLine(res);

                        if (res.Verified)
                        {




                        }

                        return;

                    }
                }

                
            }

            return;
             
            
        }
        */

        void GuardarHuella(string tabla, string nombre, Template template)
        {
            if (conexion.getConexion() == null)
            {
                Console.WriteLine("No se conecto a la base de datos");
                return;
            }

            string consulta = $"INSERT INTO " + tabla + "  (Nombre, Huella1) VALUES (@Nombre, @Huella1)";
            MySqlCommand comando = new MySqlCommand(consulta, conexion.getConexion());
            comando.Parameters.AddWithValue("@Nombre", nombre);
            comando.Parameters.AddWithValue("@Huella1", template.Bytes);
            comando.ExecuteReader();
            comando.ExecuteReader().Close();
        }

        void OutputData()
        {
            Console.WriteLine("Templates de Data: ");
            Console.WriteLine(Data.Templates);
        }

        private AppData Data;
        private Conexion conexion = new Conexion();
        
    }
}