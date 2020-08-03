using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Controllers
{
    [Route("api/{countryId}/regions")]
    [ApiController]
    public class RegionsController : ControllerBase
    {
        private readonly IDataHelper data;

        public RegionsController(IDataHelper data)
        {            
            this.data = data;
        }

        // GET: api/Regions
        [HttpGet]
        public ActionResult<IEnumerable<Region>> GetRegions(int countryId)
        {
            return Ok(data.GetRegions(countryId));
        }

        // GET: api/Regions/5
        [HttpGet("{id}")]
        public ActionResult<Region> GetRegion(int id)
        {

            return Ok(data.GetRegion(id));
        }

    }
}
