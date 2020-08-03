using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace Ds4At6.Api
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            var ConnectionString = this.Configuration.GetConnectionString("DefaultConnection");

            services.AddDbContext<DataContext>(options =>
                options.UseSqlServer(ConnectionString));

            services.AddHttpContextAccessor();
            services.AddScoped<IDataHelper, DataHelper>();
            services.AddControllers();
            services.AddSwaggerDocument(settings =>
            {
                settings.Title = "DS4All Team 6 - Minjusticia";
                settings.Version = "1.0";
                settings.Description = "API for the final project for the DS4All Colombia course";
                settings.PostProcess = document =>
                {
                    //document.Info.Version = "v1";
                    //document.Info.Title = "ToDo API";
                    //document.Info.Description = "A simple ASP.NET Core web API";
                    //document.Info.TermsOfService = "None";
                    //document.Info.Contact = new NSwag.OpenApiContact
                    //{
                    //    Name = "Shayne Boyer",
                    //    Email = string.Empty,
                    //    Url = "https://twitter.com/spboyer"
                    //};
                    //document.Info.License = new NSwag.OpenApiLicense
                    //{
                    //    Name = "Use under LICX",
                    //    Url = "https://example.com/license"
                    //};
                };
            }           
            );
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseAuthorization();

            app.UseOpenApi();
            app.UseSwaggerUi3();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
