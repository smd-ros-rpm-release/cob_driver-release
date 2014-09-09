Name:           ros-indigo-cob-canopen-motor
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS cob_canopen_motor package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_canopen_motor
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-generic-can
Requires:       ros-indigo-cob-utilities
Requires:       ros-indigo-roscpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-generic-can
BuildRequires:  ros-indigo-cob-utilities
BuildRequires:  ros-indigo-roscpp

%description
The package cob_canopen_motor implements a controller-drive component which is
connected to a can-bus and works with a canopen-interface.
&quot;CanDriveItf&quot; provides a - more or less - generic interface to the
controller-drive components. &quot;CanDrvie...&quot; then implements a specific
setup, e.g. an ELMO Harmonica Controller in case of the
&quot;CanDriveHarmonica&quot;.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 09 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

