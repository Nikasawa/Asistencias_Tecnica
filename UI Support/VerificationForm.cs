using MySql.Data.MySqlClient;
using System;
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
      
        // sigo cuando me agarre un pedo
    
      // Compare feature set with all stored templates.
      foreach (DPFP.Template template in Data.Templates) {

        // Get template from storage.
        if (template != null) {

          // Compare feature set with particular template.
          ver.Verify(FeatureSet, template, ref res);
          Data.IsFeatureSetMatched = res.Verified;
          Data.FalseAcceptRate = res.FARAchieved;

                    if (res.Verified)
                    {
                        if(conexion.getConexion() == null)
                        {
                            Console.WriteLine("No se conecto a la base de datos");
                            break;
                        }

                        string consulta = $"INSERT INTO pruebahuella (Nombre, Huella1) VALUES (@Nombre, @Huella1)";
                        MySqlCommand comando = new MySqlCommand(consulta, conexion.getConexion());
                        comando.Parameters.AddWithValue("@Nombre", "PollaBullrich");
                        comando.Parameters.AddWithValue("@Huella1", template.Bytes);
                        comando.ExecuteReader();

                        break; // success
                    }
        }
      }

      if (!res.Verified)
        Status = DPFP.Gui.EventHandlerStatus.Failure;

      Data.Update();
    }

        private AppData Data;
        private Conexion conexion = new Conexion();
        
    }
}