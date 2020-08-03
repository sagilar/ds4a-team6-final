using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Models.ViewModels
{
    public class RegionViewModel
    {
        public int RegionId { get; set; }

        public string Name { get; set; }

        public double Gnic { get; set; }

        public double Population { get; set; }
    }
}
