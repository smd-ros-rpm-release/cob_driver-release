Name:           ros-indigo-cob-voltage-control
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS cob_voltage_control package

Group:          Development/Libraries
License:        LGPL
URL:            None
Source0:        %{name}-%{version}.tar.gz

Requires:       blt
Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-phidgets
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-libphidgets
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       tcl
Requires:       tix
Requires:       tk
BuildRequires:  blt
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-msgs
BuildRequires:  ros-indigo-cob-phidgets
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-libphidgets
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  tcl
BuildRequires:  tix
BuildRequires:  tk

%description
Interface to IO board that manages emergency stop and battery voltage on
rob@work 3

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 15 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

