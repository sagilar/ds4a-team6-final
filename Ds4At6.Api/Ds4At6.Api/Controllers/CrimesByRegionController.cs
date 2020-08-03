using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace Ds4At6.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CrimesByRegionController : ControllerBase
    {
        private readonly IDataHelper data;

        public CrimesByRegionController(IDataHelper data)
        {
            this.data = data;
        }

        [HttpGet]
        public ActionResult<IEnumerable<CrimesByRegionViewModel>> GetCrime()
        {
            return Ok(this.data.GetCrimesByRegion());
        }
    }
}
