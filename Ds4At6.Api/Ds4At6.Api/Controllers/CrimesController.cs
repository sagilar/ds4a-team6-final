using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace Ds4At6.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CrimesController : ControllerBase
    {
        private readonly IDataHelper data;

        public CrimesController(IDataHelper data)
        {
            this.data = data;
        }

        [HttpGet]
        public ActionResult<IEnumerable<CrimeViewModel>> GetCrime()
        {
            return Ok(this.data.GetCrimes());
        }
    }
}
