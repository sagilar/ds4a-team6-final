using Ds4At6.Api.Models.ViewModels;
using System.Collections.Generic;

namespace Ds4At6.Api.Helpers
{
    public interface IDataHelper
    {
        List<CrimesByRegionViewModel> GetCrimesByRegion();

        List<CrimesByScholarshipViewModel> GetCrimesByScholarship();

        List<CrimesByMaritalStatusViewModel> GetCrimesByMaritalStatus();

        List<PersonAttributesViewModel> GetPersonsWithKids();

        List<PersonAttributesViewModel> GetPersonsBySex();

        List<PersonAttributesViewModel> GetPersonsByAgeAndGender();

        List<PersonAttributesViewModel> GetPersonsBySpecialCondition();

        List<CrimeViewModel> GetCrimes();

        List<RegionViewModel> GetRegions(int countryId);

        RegionViewModel GetRegion(int regionId);
    }
}