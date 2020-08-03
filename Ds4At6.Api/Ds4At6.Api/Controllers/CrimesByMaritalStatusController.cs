using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace Ds4At6.Api.Models.ViewModels
{
    [Route("api/[controller]")]
    [ApiController]

    public class CrimesByMaritalStatusController : ControllerBase
    {
        private readonly IDataHelper data;

        public CrimesByMaritalStatusController(IDataHelper data)
        {
            this.data = data;
        }

        [HttpGet]
        public ActionResult<IEnumerable<CrimesByMaritalStatusViewModel>> GetCrime()
        {
            return Ok(this.data.GetCrimesByMaritalStatus());
        }
    }
}
