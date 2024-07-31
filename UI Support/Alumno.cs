using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UI_Support
{
    public class Alumno
    {
        // Clase constructora para hacer toda la entidad de alumno
        // Dejo las variables de huellas comentadas
        // porque no estoy seguro de que sean necesarias en alguna funcion
        public Alumno(int ID, string nombre, string apellido/*, byte[] huella1, byte[] huella2, byte[] huella3, byte[] huella4*/)
        {
            ID = ID;
            nombre = nombre;
            apellido = apellido;
            //huella1 = huella1;
            //huella2 = huella2;
            //huella3 = huella3;
            //huella4 = huella4;
        }



        // Funcion para mostrar la proxima clase, profesor y materia del alumno.
        public void MostarProxClase()
        {

        }

        // Funcion para mostrar todos los datos del alumno
        public void Output(Alumno)
        {
            Console.WriteLine($"ID: {this.ID}");
            Console.WriteLine($"Nombre: {this.nombre}");
            Console.WriteLine($"Apellido: {this.apellido}");
        }
    }

}
