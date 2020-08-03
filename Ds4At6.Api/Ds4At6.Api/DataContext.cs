using Microsoft.EntityFrameworkCore;

namespace Ds4At6.Api.Models
{
    public partial class DataContext : DbContext
    {
        public DataContext()
        {
        }

        public DataContext(DbContextOptions<DataContext> options)
            : base(options)
        {
        }

        public virtual DbSet<CitiesView> CitiesView { get; set; }
        public virtual DbSet<City> City { get; set; }
        public virtual DbSet<Country> Country { get; set; }
        public virtual DbSet<Crime> Crime { get; set; }
        public virtual DbSet<CrimeGroup> CrimeGroup { get; set; }
        public virtual DbSet<Gender> Gender { get; set; }
        public virtual DbSet<MaritalStatus> MaritalStatus { get; set; }
        public virtual DbSet<Person> Person { get; set; }
        public virtual DbSet<PersonCondition> PersonCondition { get; set; }
        public virtual DbSet<Prison> Prison { get; set; }
        public virtual DbSet<Reclusion> Reclusion { get; set; }
        public virtual DbSet<ReclusionStatus> ReclusionStatus { get; set; }
        public virtual DbSet<Region> Region { get; set; }
        public virtual DbSet<Regional> Regional { get; set; }
        public virtual DbSet<RegionsView> RegionsView { get; set; }
        public virtual DbSet<Scholarship> Scholarship { get; set; }
        public virtual DbSet<SpecialCondition> SpecialCondition { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<CitiesView>(entity =>
            {
                entity.HasNoKey();

                entity.ToView("CitiesView");

                entity.Property(e => e.CityName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.CountryName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.RegionName)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<City>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);

               
            });

            modelBuilder.Entity<Country>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Crime>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<CrimeGroup>(entity =>
            {
                entity.HasKey(e => e.GroupId)
                    .HasName("PK__CrimeGro__149AF36A5C86FC4B");

                entity.Property(e => e.Group)
                    .IsRequired()
                    .HasMaxLength(200)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Gender>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(20)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<MaritalStatus>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(20)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Person>(entity =>
            {
                entity.HasIndex(e => e.RemoteId)
                    .HasName("UQ__Person__9EFEB0C517FB1AE5")
                    .IsUnique();

                entity.Property(e => e.AdultoMayor).HasColumnName("ADULTO MAYOR");

                entity.Property(e => e.AfroColombiano).HasColumnName("AFRO COLOMBIANO");

                entity.Property(e => e.Bisexual).HasColumnName("BISEXUAL");

                entity.Property(e => e.ConDiscapacidad).HasColumnName("CON DISCAPACIDAD");

                entity.Property(e => e.Extranjeros).HasColumnName("EXTRANJEROS");

                entity.Property(e => e.Gays).HasColumnName("GAYS");

                entity.Property(e => e.HasKids)
                    .HasMaxLength(2)
                    .IsUnicode(false);

                entity.Property(e => e.Indigena).HasColumnName("INDIGENA");

                entity.Property(e => e.Intersexual).HasColumnName("INTERSEXUAL");

                entity.Property(e => e.Lesbiana).HasColumnName("LESBIANA");

                entity.Property(e => e.MadreGestante).HasColumnName("MADRE GESTANTE");

                entity.Property(e => e.MadreLactante).HasColumnName("MADRE LACTANTE");

                entity.Property(e => e.Raizales).HasColumnName("RAIZALES");

                entity.Property(e => e.RemoteId)
                    .IsRequired()
                    .HasMaxLength(40)
                    .IsUnicode(false);

                entity.Property(e => e.Rom).HasColumnName("ROM");

                entity.Property(e => e.Transexual).HasColumnName("TRANSEXUAL");

              
            });

            

            modelBuilder.Entity<Prison>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(180)
                    .IsUnicode(false);

            
            });

            modelBuilder.Entity<Reclusion>(entity =>
            {
                entity.HasNoKey();

                entity.HasIndex(e => e.PersonId)
                    .HasName("IX_PersonId");

                entity.Property(e => e.CaptureDate).HasColumnType("date");

                entity.Property(e => e.EndDate).HasColumnType("date");

                entity.Property(e => e.ReclusionId).ValueGeneratedOnAdd();

                entity.Property(e => e.StartDate).HasColumnType("date");

            });

            modelBuilder.Entity<ReclusionStatus>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Region>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                
            });

            modelBuilder.Entity<Regional>(entity =>
            {
                entity.Property(e => e.Name)
                    .IsRequired()
                    .HasMaxLength(50)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<RegionsView>(entity =>
            {
                entity.HasNoKey();

                entity.ToView("RegionsView");

                entity.Property(e => e.CountryName)
                    .HasMaxLength(60)
                    .IsUnicode(false);

                entity.Property(e => e.RegionName)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<Scholarship>(entity =>
            {
                entity.Property(e => e.Name)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<SpecialCondition>(entity =>
            {
                entity.Property(e => e.Condition)
                    .HasMaxLength(60)
                    .IsUnicode(false);
            });

            

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
