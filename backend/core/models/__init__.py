from typing import Type

from django.db.models import QuerySet

from core.exceptions.model_not_found_exception import ModelNotFoundException
from core.exceptions.authorization_rule_exception import AuthorizationRuleException

from .album.album_favorite_model import AlbumFavorite
from .album.album_comment_model import AlbumComment
from .album.album_like_model import AlbumLike
from .album.album_media_model import AlbumMedia
from .album.album_model import Album

from .comment.comment_like_model import CommentLike
from .comment.comment_model import Comment

from .company.company_information_model import CompanyInformation
from .company.company_model import Company
from .company.company_paint_scheme_information_model import CompanyPaintSchemeInformation
from .company.company_paint_scheme_model import CompanyPaintScheme

from .contact.contact_model import Contact

from .freight_car.freight_car_category_model import FreightCarCategory
from .freight_car.freight_car_gross_weight_type_model import FreightCarGrossWeightType
from .freight_car.freight_car_model import FreightCar
from .freight_car.freight_car_type_model import FreightCarType

from .generic_audited_model import GenericAuditedModel

from .information.information_effect_model import InformationEffect
from .information.information_like_model import InformationLike
from .information.information_model import Information
from .information.information_vote_model import InformationVote

from .location.location_city_model import LocationCity
from .location.location_information_model import LocationInformation
from .location.location_model import Location
from .location.location_path_model import LocationPath
from .location.location_state_model import LocationState
from .location.location_track_gauge_model import LocationTrackGauge

from .locomotive.locomotive_design_gauge_model import LocomotiveDesignGauge
from .locomotive.locomotive_design_model import LocomotiveDesign
from .locomotive.locomotive_model import Locomotive

from .mail.mail_model import Mail

from .manufacturer.manufacturer_information_model import ManufacturerInformation
from .manufacturer.manufacturer_model import Manufacturer

from .media.media_comment_model import MediaComment
from .media.media_document_model import MediaDocument
from .media.media_favorite_model import MediaFavorite
from .media.media_image_model import MediaImage
from .media.media_image_sized_model import MediaImageSized
from .media.media_like_model import MediaLike
from .media.media_model import Media
from .media.media_review_model import MediaReview
from .media.media_rolling_stock_model import MediaRollingStock
from .media.media_video_model import MediaVideo

from .non_revenue_car.non_revenue_car_model import NonRevenueCar
from .non_revenue_car.non_revenue_car_type_model import NonRevenueCarType

from .passenger_car.passenger_car_material_model import PassengerCarMaterial
from .passenger_car.passenger_car_model import PassengerCar
from .passenger_car.passenger_car_type_model import PassengerCarType

from .path.path_model import Path
from .path.path_point_model import PathPoint

from .rolling_stock.rolling_stock_model import RollingStock
from .rolling_stock.rolling_stock_information_model import RollingStockInformation

from .route.route_information_model import RouteInformation
from .route.route_model import Route
from .route.route_section_information_model import RouteSectionInformation
from .route.route_section_location_kilometer_model import RouteSectionLocationKilometer
from .route.route_section_location_model import RouteSectionLocation
from .route.route_section_model import RouteSection
from .route.route_section_path_model import RouteSectionPath

from .sigo.sigo_regional_model import SigoRegional
from .sigo.sigo_series_information_model import SigoSeriesInformation

from .track_gauge.track_gauge_model import TrackGauge

from .user.user_model import User
from .user.user_token_model import UserToken


def get_object_or_error(queryset: QuerySet, error_message: str = "", *args, **kwargs):
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise ModelNotFoundException(details=error_message)


def ensure_object_owner_or_deny(
        user: User,
        model_type: Type[GenericAuditedModel],
        pk: str,
        owner_field: str = 'created_by',
):
    instance = get_object_or_error(model_type.objects.all(), pk=pk)

    if not user.is_staff and not user.is_admin and getattr(instance, owner_field) != user:
        raise AuthorizationRuleException("You don't have enough permissions to perform the requested operation.")
