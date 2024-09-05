using System;
using System.Net;
using System.Net.Mail;

namespace UI_Support
{
    class Email
    {
        static void Main()
        {
            // Conexion con BD en SQL
            conexion.getConexion();

            // ayyyyyyyyy me 
            // quedo en escalera
            string consulta = null;
            MySqlCommand comando = null;
            MySqlDataReader resultado = null;   

            // Generar codigo de validacion
            while (true) 
            {
                Random random = new Random();
                string[] abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'p', 'v', 'w', 'x', 'y', 'z']; // Puse el abc de memoria soy un animal (Revisar por las dudas).
                string letraElegida;
                int numeroRandom;
                int contador;
                string codigo;

                // Elegir 5 letras o numeros aleatorios
                while (contador < 5)
                {
                    numeroRandom = random.Next(0, 2); 

                    // Si es 0 se elegie una letra del abc, si no, un numero entre el 0 y el 9
                    if(numeroRandomRandom > 0)
                    {
                        numeroRandom = random.Next(0, 28); // Si no mal recuerdo tenia 27 letras el abc. CREO que el random elige hasta un numero antes del segundo parametro de entrada.
                        letraElegida = abecedario[numeroRandom];
                        codigo += letraElegida;
                    } 
                    else 
                    {
                        numeroRandom = random.Next(0, 10); 
                        codigo += numeroRandom.toString();
                    }          
                    contador++;
                }

                // Revisar que el codigo no este en la base de datos
                consulta = "SELECT * FROM codigo WHERE codigo = @codigo"; // Revisar en codigo donde codigo sea igual a codigo :D.
                using(comando = new MySqlCommand(conexion, consulta))
                {
                    comando.Parameters.AddWithValue("@codigo", codigo);
                    resultado = comando.ExecuteReader();
                }

                // Si no encontro ningun codigo igual en la BD, lo añade y lo envia por correo
                if(!resultado.Read()) 
                {
                    // Guardar codigo en la base de datos
                    consulta = "INSERT INTO codigoCambios (fechaInicio, correoDestinatario, codigo) VALUES (NOW(), @CorreoDestinatario, @codigo))"; // Hace falta tomar la hora actual para evitar que se use con posterioridad.
                    using(comando = new MySqlCommand(conexion, consulta))
                    {
                        comando.Parameters.AddWithValue("@codigo", codigo);
                        comando.ExecuteReader();

                        // Despues se lleva a la parte donde se pida el codigo creado y se compara la hora tomada aca, con la hora que sea al ingresar el codigo.
                        // Si hay una diferencia muy grande entre los dos horarios el codigo creado ya no sera valido y el usuario tendra que pedir otro.
                        // Deberia tener un campo la base de datos para especificar que un codigo es valido o no?
                        // Seria un campo calculado? En realidad el campo que necesita es la hora a la que se creo, y en otro campo revisar si dicha hora paso hace mucho tiempo o no
                    }

                    break;
                }
            }       

            // Configuración del servidor SMTP
            string smtpAddress = "smtp.gmail.com"; // Dominio gratuito que ofrece Gmail
            int portNumber = 587; // Puerto 587 para TLS o 465 para SSL (Ni idea, esto lo puso ChatGPT)
            bool enableSSL = true;

            // Credenciales de la cuenta de correo
            string emailFrom = "huellatesteo@gmail.com"; // Correo desde donde se envia. Este es de prueba, supongo que despues hay que usar el de la escuela
            string password = "testeo1234"; // Contraseña de dicho correo
            string emailTo = "pollyvalentin@gmail.com"; // Destinatario
            string subject = "Codigo de recuperacion de contraseña"; // Asunto del correo
            string body = "El codigo para reestablecer la contraseña: " + codigo;

            // Enviar correo electronico
            using (MailMessage mail = new MailMessage())
            {
                mail.From = new MailAddress(emailFrom);
                mail.To.Add(emailTo);
                mail.Subject = subject;
                mail.Body = body;
                mail.IsBodyHtml = true; // Si el cuerpo es HTML (No se que quise poner aca pero capaz intente decir que front podria hacer un trabajito con el correo para que se vea bonito :D).

                using (SmtpClient smtp = new SmtpClient(smtpAddress, portNumber))
                {
                    smtp.Credentials = new NetworkCredential(emailFrom, password);
                    smtp.EnableSsl = enableSSL; // Ni la mas palida idea :D

                    try
                    {
                        smtp.Send(mail);
                        Console.WriteLine("Correo enviado exitosamente.");
                        
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error al enviar el correo: {ex.Message}");
                    }
                }
            }
        }

        private Conexion conexion = new Conexion();
    }
    
}