PATCH := patch
PATCH_VERS := 2.7.6
PATCH_DIR := $(PATCH)-$(PATCH_VERS)
# Increase this to enforce a recreation of the build cache
PATCH_BUILD_ID := 0

PATCH_UNPACK := $(BUILD_HELPER_DIR)/$(PATCH_DIR)-unpack
PATCH_BUILD := $(BUILD_HELPER_DIR)/$(PATCH_DIR)-build
PATCH_INTERMEDIATE_INSTALL := $(BUILD_HELPER_DIR)/$(PATCH_DIR)-install-intermediate
PATCH_CACHE_PKG_PROCESS := $(BUILD_HELPER_DIR)/$(PATCH_DIR)-cache-pkg-process
PATCH_INSTALL := $(BUILD_HELPER_DIR)/$(PATCH_DIR)-install

PATCH_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(PATCH_DIR)
PATCH_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(PATCH_DIR)
#PATCH_WORK_DIR := $(PACKAGE_WORK_DIR)/$(PATCH_DIR)

.PHONY: $(PATCH)-clean

PATCH_CACHE_PKG_PATH := $(call cache_pkg_path,$(PATCH_DIR),$(PATCH_BUILD_ID))

$(PATCH_CACHE_PKG_PATH):
	$(call pack_pkg_archive,$@,$(PATCH_DIR),$(PATCH_BUILD_ID),$(PATCH_INTERMEDIATE_INSTALL))

$(PATCH_CACHE_PKG_PROCESS): $(PATCH_CACHE_PKG_PATH)
	$(call unpack_pkg_archive,$(PATCH_CACHE_PKG_PATH),$(PATCH_DIR))
	$(call upload_pkg_archive,$(PATCH_CACHE_PKG_PATH),$(PATCH_DIR),$(PATCH_BUILD_ID))
	$(TOUCH) $@

$(PATCH_BUILD): $(PATCH_UNPACK)
	cd $(PATCH_BUILD_DIR) && ./configure --prefix=""
	$(MAKE) -C $(PATCH_BUILD_DIR)
	$(TOUCH) $@

$(PATCH_INTERMEDIATE_INSTALL): $(PATCH_BUILD)
	$(MAKE) DESTDIR=$(PATCH_INSTALL_DIR) -C $(PATCH_BUILD_DIR) install
	$(TOUCH) $@

$(PATCH_INSTALL): $(PATCH_CACHE_PKG_PROCESS)
	$(RSYNC) $(PATCH_INSTALL_DIR)/ $(DESTDIR)$(OMD_ROOT)/
	$(TOUCH) $@

$(PATCH)-clean:
	rm -rf $(PATCH_BUILD_DIR) $(BUILD_HELPER_DIR)/$(PATCH)*
