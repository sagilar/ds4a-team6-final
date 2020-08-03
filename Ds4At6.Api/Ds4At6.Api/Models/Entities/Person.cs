using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Person
    {
      

        public int PersonId { get; set; }
        public string RemoteId { get; set; }
        public int? YearBorn { get; set; }
        public int? GenderId { get; set; }
        public int? CityId { get; set; }
        public int? MaritalStatusId { get; set; }
        public int? ScholarshipId { get; set; }
        public string HasKids { get; set; }
        public int? CountryId { get; set; }
        public int? RegionId { get; set; }
        public bool? AdultoMayor { get; set; }
        public bool? AfroColombiano { get; set; }
        public bool? Bisexual { get; set; }
        public bool? ConDiscapacidad { get; set; }
        public bool? Extranjeros { get; set; }
        public bool? Gays { get; set; }
        public bool? Indigena { get; set; }
        public bool? Intersexual { get; set; }
        public bool? Lesbiana { get; set; }
        public bool? MadreGestante { get; set; }
        public bool? MadreLactante { get; set; }
        public bool? Raizales { get; set; }
        public bool? Rom { get; set; }
        public bool? Transexual { get; set; }

        
    }
}
