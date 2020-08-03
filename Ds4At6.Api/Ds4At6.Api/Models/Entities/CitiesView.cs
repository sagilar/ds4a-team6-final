using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class CitiesView
    {
        public int CountryId { get; set; }
        public int? RegionId { get; set; }
        public int? CityId { get; set; }
        public string CountryName { get; set; }
        public string RegionName { get; set; }
        public string CityName { get; set; }
    }
}
