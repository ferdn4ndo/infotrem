from django.db.models import QuerySet

from api.errors.not_found_exception import NotFoundException

from .album_comment_model import AlbumComment
from .album_favorite_model import AlbumFavorite
from .album_like_model import AlbumLike
from .album_media_model import AlbumMedia
from .album_model import Album
from .comment_like_model import CommentLike
from .comment_model import Comment
from .company_information_model import CompanyInformation
from .company_model import Company
from .company_paint_scheme_model import CompanyPaintScheme
from .company_paint_scheme_information_model import CompanyPaintSchemeInformation
from .contact_model import Contact
from .freight_car_category_model import FreightCarCategory
from .freight_car_gross_weight_type_model import FreightCarGrossWeightType
from .freight_car_model import FreightCar
from .freight_car_type_model import FreightCarType
from .information_effect_model import InformationEffect
from .information_model import Information
from .information_vote_model import InformationVote
from .location_city_model import LocationCity
from .location_information_model import LocationInformation
from .location_model import Location
from .location_path_model import LocationPath
from .location_state_model import LocationState
from .location_track_gauge_model import LocationTrackGauge
from .locomotive_design_gauge_model import LocomotiveDesignGauge
from .locomotive_design_model import LocomotiveDesign
from .locomotive_model import Locomotive
from .mail_model import Mail
from .manufacturer_information_model import ManufacturerInformation
from .manufacturer_model import Manufacturer
from .media_comment_model import MediaComment
from .media_document_model import MediaDocument
from .media_favorite_model import MediaFavorite
from .media_image_model import MediaImage
from .media_image_sized_model import MediaImageSized
from .media_like_model import MediaLike
from .media_model import Media
from .media_review_model import MediaReview
from .media_rolling_stock_model import MediaRollingStock
from .media_video_model import MediaVideo
from .non_revenue_car_model import NonRevenueCar
from .non_revenue_car_type_model import NonRevenueCarType
from .passenger_car_material_model import PassengerCarMaterial
from .passenger_car_model import PassengerCar
from .passenger_car_type_model import PassengerCarType
from .path_model import Path
from .path_point_model import PathPoint
from .rolling_stock_information_model import RollingStockInformation
from .rolling_stock_model import RollingStock
from .route_information_model import RouteInformation
from .route_model import Route
from .route_section_information_model import RouteSectionInformation
from .route_section_location_kilometer_model import RouteSectionLocationKilometer
from .route_section_location_model import RouteSectionLocation
from .route_section_model import RouteSection
from .route_section_path_model import RouteSectionPath
from .sigo_regional_model import SigoRegional
from .sigo_series_information_model import SigoSeriesInformation
from .track_gauge_model import TrackGauge
from .user_model import User
from .user_token_model import UserToken


def get_object_or_404(queryset: QuerySet, *args, **kwargs):
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise NotFoundException
