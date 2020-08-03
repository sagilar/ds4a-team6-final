using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Crime
    {
        public int CrimeId { get; set; }
        public string Name { get; set; }
        public int GroupId { get; set; }
    }
}
