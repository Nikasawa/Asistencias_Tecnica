using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Text;
using MySql.Data.MySqlClient;

namespace UI_Support
{
	public delegate void OnChangeHandler();
	
	// Keeps application-wide data shared among forms and provides notifications about changes
	//
	// Everywhere in this application a "document-view" model is used, and this class provides
	// a "document" part, whereas forms implement a "view" parts.
	// Each form interested in this data keeps a reference to it and synchronizes it with own 
	// controls using the OnChange() event and the Update() notificator method.
	//
	public class AppData
    {
        private string IP = "localhost";
        private string BaseDeDatos = "asistencias";
        private string Usuario = "root";
        private string password = "";
        private string cadenaConexion;
        private MySqlConnection conexion;

        public void Conexion()
        {
            cadenaConexion = "Database=" + BaseDeDatos +
                             "; DataSource=" + IP +
                             "; User Id=" + Usuario +
                             "; Password=" + password;
        }

        public MySqlConnection getConexion()
        {

            if (conexion == null)
            {
                conexion = new MySqlConnection(cadenaConexion);
                conexion.Open();
            }

            return conexion;

        }

        public const int MaxFingers = 10;
		// shared data
        public int EnrolledFingersMask = 0;
		public int MaxEnrollFingerCount = MaxFingers;
        public bool IsEventHandlerSucceeds = true;
        public bool IsFeatureSetMatched = false;
        public int FalseAcceptRate = 0;
		public DPFP.Template[] Templates = new DPFP.Template[MaxFingers]; // Cambiar por huellas almacenadas en base de datos

		// data change notification
		public void Update() { OnChange(); }		// just fires the OnChange() event
		public event OnChangeHandler OnChange;
	}
}
