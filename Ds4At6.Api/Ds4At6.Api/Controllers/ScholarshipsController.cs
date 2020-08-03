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
    public class ScholarshipsController : ControllerBase
    {
        private readonly DataContext _context;

        public ScholarshipsController(DataContext context)
        {
            _context = context;
        }

        // GET: api/Scholarships
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Scholarship>>> GetScholarship()
        {
            return await _context.Scholarship
                .OrderBy(s => s.Name)
                .ToListAsync();
        }

        // GET: api/Scholarships/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Scholarship>> GetScholarship(int id)
        {
            var scholarship = await _context.Scholarship.FindAsync(id);

            if (scholarship == null)
            {
                return NotFound();
            }

            return scholarship;
        }
    }
}
