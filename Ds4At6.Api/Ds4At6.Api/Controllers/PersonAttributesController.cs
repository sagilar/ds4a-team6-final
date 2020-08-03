using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace Ds4At6.Api.Models.ViewModels
{
    [Route("api/PersonsByAttributes")]
    [ApiController]

    public class PersonAttributesController : ControllerBase
    {
        private readonly IDataHelper data;

        public PersonAttributesController(IDataHelper data)
        {
            this.data = data;
        }

        [Route("api/[controller]/HasKids")]
        [HttpGet]
        public ActionResult<IEnumerable<PersonAttributesViewModel>> GetPersonsWithKids()
        {
            return Ok(this.data.GetPersonsWithKids());
        }

        [Route("api/[controller]/Sex")]
        [HttpGet]
        public ActionResult<IEnumerable<PersonAttributesViewModel>> GetPersonsBySex()
        {
            return Ok(this.data.GetPersonsBySex());
        }

        [Route("api/[controller]/AgeAndSex")]
        [HttpGet]
        public ActionResult<IEnumerable<PersonAttributesViewModel>> GetPersonsByAgeAndSex()
        {
            return Ok(this.data.GetPersonsByAgeAndGender());
        }

        [Route("api/[controller]/SpecialCondition")]
        [HttpGet]
        public ActionResult<IEnumerable<PersonAttributesViewModel>> GetPersonsBySpecialCondition()
        {
            return Ok(this.data.GetPersonsBySpecialCondition());
        }

    }

}
