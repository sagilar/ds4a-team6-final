using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Models.ViewModels
{
    public class PersonAttributesViewModel
    {
        public int HasKids { get; set; }

        public int Events { get; set; }

        public string Gender { get; set; }

        public int Age { get; set; }

        public string Condition { get; set; }
    }
}
