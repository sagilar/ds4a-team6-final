using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Models.ViewModels
{
    public class CrimesByRegionViewModel
    {
        public int RegionId { get; set; }

        public string Region { get; set; }

        public decimal Events { get; set; }
    }
}
