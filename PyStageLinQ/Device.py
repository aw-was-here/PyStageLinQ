from . import DataClasses

class DeviceList:

    device_list : DataClasses.StageLinQDiscoveryData

    def __init__(self):
        self.device_list = []

    def register_device(self, device):
        self.device_list.append(device)

    def find_registered_device(self, discovery_frame) -> DataClasses.StageLinQDiscoveryData:
        # Check if main link has been established for Offline analyzers
        if (
            discovery_frame.SwName == "OfflineAnalyzer"
            and not self.find_main_interface(discovery_frame)
        ):
            return True

        return any(
            discovery_frame.DeviceName == device.device_name
            and discovery_frame.ReqServicePort == device.Port
            for device in self.device_list
        )

    def find_main_interface(self, discovery_frame) -> DataClasses.StageLinQDiscoveryData:
        return any(
            device.device_name == discovery_frame.DeviceName
            and device.sw_name != "OfflineAnalyzer"
            for device in self.device_list
        )
