using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Ds4At6.Api.Models;

namespace Ds4At6.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class MaritalStatusController : ControllerBase
    {
        private readonly DataContext _context;

        public MaritalStatusController(DataContext context)
        {
            _context = context;
        }

        // GET: api/MaritalStatus
        [HttpGet]
        public async Task<ActionResult<IEnumerable<MaritalStatus>>> GetMaritalStatus()
        {
            return await _context.MaritalStatus
                .OrderBy(s => s.Name)
                .ToListAsync();
        }

        // GET: api/MaritalStatus/5
        [HttpGet("{id}")]
        public async Task<ActionResult<MaritalStatus>> GetMaritalStatus(int id)
        {
            var maritalStatus = await _context.MaritalStatus.FindAsync(id);

            if (maritalStatus == null)
            {
                return NotFound();
            }

            return maritalStatus;
        }

    }
}
