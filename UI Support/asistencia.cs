using System;
using System.Collections.Generic;
using MySql.Data.MySqlClient;

namespace AsistenciasSystem
{
    // Class to represent a student
    public class Alumno
    {
        // Attributes
        public int Falta { get; set; }
        public int FaltasJustificadas { get; set; }
        public int FaltaTotal { get; set; }
        public int Asistencias { get; set; }
        public string Dia { get; set; }
        public List<int[]> Jornada { get; set; } // List of time arrays [hour, minute]
        public List<int[]> HorarioEntrada { get; set; } // List of time arrays [hour, minute]
        public List<int[]> HorarioSalida { get; set; } // List of time arrays [hour, minute]
        public bool Entro { get; set; }
        public bool Retiro { get; set; }
        public int[] HoraLlegada { get; set; } // Time array [hour, minute]
        public int[] HoraSalida { get; set; } // Time array [hour, minute]
        public double FaltaDia { get; set; } // Accumulated fault for the day

        // Constructor
        public Alumno(int falta, int faltasJustificadas, string dia, List<int[]> jornada)
        {
            Falta = falta;
            FaltasJustificadas = faltasJustificadas;
            FaltaTotal = falta + faltasJustificadas;
            Asistencias = 28 - falta;
            Dia = dia;
            Jornada = jornada;
            HorarioEntrada = new List<int[]>();
            HorarioSalida = new List<int[]>();
            Entro = false;
            Retiro = false;
            HoraLlegada = new int[] { -1, -1 }; // Default values
            HoraSalida = new int[] { -1, -1 }; // Default values
            FaltaDia = 0;
        }

        // Method to calculate the student's entry and exit times based on the day's schedule
        public void SetHorarios()
        {
            // Horarios de salida típicos (en formato [hora, minuto])
            List<int[]> horariosSalida = new List<int[]> { new int[] { 11, 50 }, new int[] { 17, 50 }, new int[] { 22, 30 } };

            int[] horario = Jornada[0];

            foreach (int[] horaSalida in horariosSalida)
            {
                foreach (int[] hora in Jornada)
                {
                    if (CompararHoras(hora, horaSalida))
                    {
                        HorarioEntrada.Add(hora);
                        HorarioSalida.Add(horario);
                        break;
                    }

                    horario = hora;
                }
            }

            HorarioSalida.Add(Jornada[Jornada.Count - 1]);
        }

        // Method to register the student's arrival time
        public void GetHorarioLlegada()
        {
            if (Entro) return; // If the student has already entered, do nothing

            HoraLlegada = GetHoraMinuto();

            if (HoraLlegada[0] == HorarioSalida[0] && HoraLlegada[1] < HorarioSalida[1] || HoraLlegada[0] < HorarioSalida[0])
            {
                Entro = true;
            }
        }

        // Method to register the student's departure time
        public void GetHorarioSalida()
        {
            if (!Entro) return; // If the student hasn't entered, do nothing

            HoraSalida = GetHoraMinuto();

            if (HoraSalida[0] < HorarioSalida[0] || (HoraSalida[0] == HorarioSalida[0] && HoraSalida[1] < HorarioSalida[1]))
            {
                Retiro = true;
            }
        }

        // Method to calculate the student's fault for the day
        public void MedirFalta()
        {
            // Fault values
            double SinFalta = 0;
            double CuartoFalta = 0.25;
            double MediaFalta = 0.5;
            double CompletaFalta = 1;

            if (!Entro)
            {
                FaltaDia = CompletaFalta;
                return;
            }

            if (HoraLlegada[0] < HorarioEntrada[0])
            {
                FaltaDia = SinFalta;
                return;
            }

            if (HoraLlegada[0] == HorarioEntrada[0] && HoraLlegada[1] <= HorarioEntrada[1])
            {
                FaltaDia = SinFalta;
                return;
            }

            if (HoraLlegada[0] <= HorarioEntrada[0] + 1)
            {
                FaltaDia += CuartoFalta;

                int[] margenDe15Minutos = SumarMinutos(HorarioEntrada[1], 15);

                if (HoraLlegada[1] > margenDe15Minutos[1])
                {
                    FaltaDia += MediaFalta;
                }

                return;
            }

            FaltaDia += MediaFalta;
        }

        // Method to apply the accumulated fault for the day
        public void AplicarFalta()
        {
            FaltaTotal += FaltaDia;
        }

        // Method to compare two time arrays (hour, minute)
        private bool CompararHoras(int[] hora1, int[] hora2)
        {
            for (int i = 0; i < 2; i++)
            {
                if (hora1[i] > hora2[i]) return true;
                if (hora2[i] > hora1[i]) return false;
            }

            return false;
        }

        // Method to add minutes to a time array
        private int[] SumarMinutos(int minuto1, int minuto2)
        {
            int otraHora = 0;
            int minutosTotal = minuto1 + minuto2;
            const int UNA_HORA = 60;

            while (minutosTotal >= UNA_HORA)
            {
                if (minutosTotal >= UNA_HORA)
                {
                    otraHora += 1;
                    minutosTotal -= UNA_HORA;
                }
            }

            return new int[] { otraHora, minutosTotal };
        }

        // Method to get the current hour and minute
        private static int[] GetHoraMinuto()
        {
            DateTime now = DateTime.Now;
            return new int[] { now.Hour, now.Minute };
        }
    }

    // Class to represent a classroom (not implemented yet)
    public class Salon
    {
        // ...
    }

    // Class to represent a subject (not implemented yet)
    public class Materias
    {
        // ...
    }

    // Class to represent a teacher (not implemented yet)
    public class Profesor
    {
        // ...
    }

    public void datos()
    {
        // Database connection string
        private static string ConnectionString = "server=localhost;user=root;database=asistencias";

        // Dictionary to store the weekly schedule for each day (Monday, Tuesday, etc.)
        private static Dictionary<string, List<int[]>> Dias = new Dictionary<string, List<int[]>>()
        {
            { "Monday", new List<int[]> { new int[] { 7, 20 }, new int[] { 8, 30 }, new int[] { 9, 40 }, new int[] { 10, 50 }, new int[] { 11, 50 }, new int[] { 13, 20 }, new int[] { 14, 30 }, new int[] { 15, 40 }, new int[] { 16, 50 }, new int[] { 17, 50 } } },
            { "Tuesday", new List<int[]> { new int[] { 7, 20 }, new int[] { 8, 30 }, new int[] { 9, 40 }, new int[] { 10, 50 }, new int[] { 11, 50 } } },
            { "Wednesday", new List<int[]> { new int[] { 7, 20 }, new int[] { 8, 30 }, new int[] { 9, 40 }, new int[] { 10, 50 }, new int[] { 11, 50 }, new int[] { 13, 20 }, new int[] { 14, 30 }, new int[] { 15, 40 }, new int[] { 16, 50 }, new int[] { 17, 50 } } },
            { "Thursday", new List<int[]> { new int[] { 7, 20 }, new int[] { 8, 30 }, new int[] { 9, 40 }, new int[] { 10, 50 }, new int[] { 11, 50 } } },
            { "Friday", new List<int[]> { new int[] { 7, 20 }, new int[] { 8, 30 }, new int[] { 9, 40 }, new int[] { 10, 50 }, new int[] { 11, 50 } } }
        };

        static void Main(string[] args)
        {
            // Create a student instance
            Alumno juanito = new Alumno(2, 1, DateTime.Now.DayOfWeek.ToString(), Dias[DateTime.Now.DayOfWeek.ToString()]);

            // Set the student's entry and exit times
            juanito.SetHorarios();

            // Get the current time
            int[] horaActual = GetHoraMinuto();
            Console.WriteLine($"Hora actual: {horaActual[0]}:{horaActual[1]}");

            // Example of registering student's arrival
            juanito.GetHorarioLlegada();

            // Example of registering student's departure
            juanito.GetHorarioSalida();

            // Calculate and apply the student's fault for the day
            juanito.MedirFalta();
            juanito.AplicarFalta();

            // Print the student's data
            Console.WriteLine($"Faltas: {juanito.Falta}");
            Console.WriteLine($"Faltas Justificadas: {juanito.FaltasJustificadas}");
            Console.WriteLine($"Falta Total: {juanito.FaltaTotal}");
            Console.WriteLine($"Asistencias: {juanito.Asistencias}");
            Console.WriteLine($"Dia: {juanito.Dia}");
            Console.WriteLine($"Jornada: {string.Join(", ", juanito.Jornada)}");
            Console.WriteLine($"Horario Entrada: {string.Join(", ", juanito.HorarioEntrada)}");
            Console.WriteLine($"Horario Salida: {string.Join(", ", juanito.HorarioSalida)}");
            Console.WriteLine($"Entro: {juanito.Entro}");
            Console.WriteLine($"Retiro: {juanito.Retiro}");
            Console.WriteLine($"Hora Llegada: {juanito.HoraLlegada[0]}:{juanito.HoraLlegada[1]}");
            Console.WriteLine($"Hora Salida: {juanito.HoraSalida[0]}:{juanito.HoraSalida[1]}");
            Console.WriteLine($"Falta Dia: {juanito.FaltaDia}");


            Console.ReadLine(); // Wait for user input before closing
        }
    }
}