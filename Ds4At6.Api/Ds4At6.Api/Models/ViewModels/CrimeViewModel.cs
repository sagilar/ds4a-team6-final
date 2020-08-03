using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Threading.Tasks;

namespace Ds4At6.Api.Models.ViewModels
{
    public class CrimeViewModel
    {
        public int CrimeId { get; set; }

        public string Name { get; set; }

        public int Weight { get; set; }
    }
}
