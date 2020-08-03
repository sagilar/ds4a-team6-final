using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Reclusion
    {
        public int ReclusionId { get; set; }
        public int PersonId { get; set; }
        public int CrimeId { get; set; }
        public bool IsAttempt { get; set; }
        public bool IsAggravated { get; set; }
        public bool IsQualified { get; set; }
        public DateTime StartDate { get; set; }
        public DateTime? EndDate { get; set; }
        public DateTime CaptureDate { get; set; }
        public int? ReclusionStatusId { get; set; }
        public bool DoWork { get; set; }
        public bool DoStudy { get; set; }
        public bool DoTeaching { get; set; }
        public int PrisonId { get; set; }
        public bool IsActive { get; set; }

     
    }
}
