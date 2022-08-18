from uuid import uuid4
from pydantic import Field
from decimal import Decimal
from pydantic import BaseModel
from pydantic.types import UUID4
from typing import List, Optional,Any

from app.repository.claims import ClaimsRepository


class ClaimsModel(BaseModel):
    id: Optional[UUID4] = None
    typeCode: Optional[str] = None
    statusCode: Optional[str] = None
    statusTypeCode: Optional[Any] = None
    prescriptionNumber: Optional[str] = None
    ndc: Optional[str] = None
    gcn: Optional[str] = None
    productLabelName: Optional[str] = None
    serviceDate: Optional[str] = None
    processDate: Optional[Any] = None
    adjustedDate: Optional[Any] = None
    updatedDate: Optional[Any] = None
    originTypeCode: Optional[Any] = None
    pharmacyName: Optional[str] = None
    pharmacyNcpdpId: Optional[str] = None
    pharmacyNpi: Optional[str] = None
    cignaHomeDeliveryPharmacyIndicator: Optional[str] = None
    pharmacyNetworkCoverageTypeCode: Optional[str] = None
    memberName: Optional[str] = None
    memberAmi: Optional[str] = None
    memberId: Optional[str] = None
    accountId: Optional[str] = None
    accountName: Optional[str] = None
    lineOfBusinessCode: Optional[str] = None
    preauthorizationNumber: Optional[Any] = None
    submittedPreauthorizationNumber: Optional[Any] = None
    medicaidClaimNumber: Optional[Any] = None
    outOfPocketTypeCode: Optional[Any] = None
    umPackageTokenId: Optional[Any] = None
    umPackageMajorVersionId: Optional[Any] = None
    umPackageMinorVersionId: Optional[Any] = None
    umProgramId: Optional[Any] = None
    umProgramMajorVersionId: Optional[Any] = None
    umProgramMinorVersionId: Optional[Any] = None
    umProgramTypeCode: Optional[Any] = None
    umProgramCategoryCode: Optional[Any] = None
    sequenceNumber: Optional[Any] = None
    dispenseStatusCode: Optional[Any] = None
    delayReasonCode: Optional[Any] = None
    preauthorizationEffectiveDate: Optional[Any] = None
    preauthorizationExpirationDate: Optional[Any] = None
    receivedDate: Optional[str] = None
    originalClaimReceivedDate: Optional[Any] = None
    injuryDate: Optional[Any] = None
    preauthorizationReasonCode: Optional[Any] = None
    gapDiscountPlanOverrideCode: Optional[Any] = None
    authorizedRefillsNumber: Optional[Any] = None
    medicareTransplantCoverageCode: Optional[Any] = None
    directMemberReimbursementClaimId: Optional[Any] = None
    directMemberReimbursementReceivedDate: Optional[Any] = None
    versionCode: Optional[Any] = None
    medicareClaimProcessTypeCode: Optional[Any] = None
    catastrophicCoverageCode: Optional[Any] = None
    submissionClarificationCode: Optional[Any] = None
    trueOutOfPocketEligibleIndicator: Optional[Any] = None
    retireeDrugSubsidyIndicator: Optional[Any] = None
    vendorClaimId: Optional[Any] = None
    priceSourceCode: Optional[Any] = None
    associatedPriceSourceCode: Optional[Any] = None
    cmsProcessIndicator: Optional[Any] = None
    financialCycleEndDate: Optional[Any] = None
    providerServiceTypeCode: Optional[Any] = None
    coordinationOfBenefitTypeCode: Optional[Any] = None
    submittedCoordinationOfBenefitTypeCode: Optional[Any] = None
    hospiceStatusCode: Optional[Any] = None
    trueOutOfPocketDeductibleStatusCode: Optional[Any] = None
    copayCalculationBasisCode: Optional[Any] = None
    dispensingFeeCalculationBasisCode: Optional[Any] = None
    coinsuranceCalculationBasisCode: Optional[Any] = None
    cmsPartDDefinedQualifiedFacilityCode: Optional[Any] = None
    medicaidPaidDate: Optional[Any] = None
    matchedDate: Optional[Any] = None
    paidDate: Optional[Any] = None
    unitOfMeasureCode: Optional[Any] = None
    compoundClaimIndicator: Optional[str] = None
    benefitManagementSystemCode: Optional[str] = None
    deductiblePlanTypeCode: Optional[Any] = None
    checkNumber: Optional[Any] = None
    member: Optional[Any] = None
    prescription: Optional[Any] = None
    financial: Optional[Any] = None
    prescriber: Optional[Any] = None
    pharmacy: Optional[Any] = None
    errors: Optional[Any] = None
    notes: Optional[Any] = None
    diagnoses: Optional[Any] = None
    extensions: Optional[Any] = None

class ClaimsDomain():
    def __init__(self, repository: ClaimsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_claim(self, id: str):
        return self.__repository.get_claim(id)

    def create_claim(self, claim: ClaimsModel):
        claim.id = str(uuid4())
        return self.__repository.create_claim(claim.dict())

    def update_claim(self, claim: ClaimsModel):
        return self.__repository.update_claim(claim.dict())

    def delete_claim(self, id: str):
        return self.__repository.delete_claim(id)