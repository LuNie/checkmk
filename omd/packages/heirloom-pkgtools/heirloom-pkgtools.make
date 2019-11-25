HEIRLOOM_PKGTOOLS := heirloom-pkgtools
HEIRLOOM_PKGTOOLS_VERS := 070227
HEIRLOOM_PKGTOOLS_DIR := $(HEIRLOOM_PKGTOOLS)-$(HEIRLOOM_PKGTOOLS_VERS)

HEIRLOOM_PKGTOOLS_PATCHING := $(BUILD_HELPER_DIR)/$(HEIRLOOM_PKGTOOLS_DIR)-patching
HEIRLOOM_PKGTOOLS_BUILD := $(BUILD_HELPER_DIR)/$(HEIRLOOM_PKGTOOLS_DIR)-build
HEIRLOOM_PKGTOOLS_INSTALL := $(BUILD_HELPER_DIR)/$(HEIRLOOM_PKGTOOLS_DIR)-install

#HEIRLOOM_PKGTOOLS_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(HEIRLOOM_PKGTOOLS_DIR)
HEIRLOOM_PKGTOOLS_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(HEIRLOOM_PKGTOOLS_DIR)
#HEIRLOOM_PKGTOOLS_WORK_DIR := $(PACKAGE_WORK_DIR)/$(HEIRLOOM_PKGTOOLS_DIR)

.PHONY: $(HEIRLOOM_PKGTOOLS)-clean

$(HEIRLOOM_PKGTOOLS_BUILD): $(HEIRLOOM_PKGTOOLS_PATCHING)
	cd $(HEIRLOOM_PKGTOOLS_BUILD_DIR) ; \
	    find -name Makefile -delete ; \
	    $(MAKE) -j 1
	$(TOUCH) $@

$(HEIRLOOM_PKGTOOLS_INSTALL): $(HEIRLOOM_PKGTOOLS_BUILD)
	for F in pkgmk pkgtrans; do \
	    install -m 755 $(HEIRLOOM_PKGTOOLS_BUILD_DIR)/pkgcmds/$$F/$$F $(DESTDIR)$(OMD_ROOT)/bin/ ; \
	    install -m 644 $(HEIRLOOM_PKGTOOLS_BUILD_DIR)/man/$$F.1 $(DESTDIR)$(OMD_ROOT)/share/man/man1/; \
	    gzip -f $(DESTDIR)$(OMD_ROOT)/share/man/man1/$$F.1 ; \
	done
	$(TOUCH) $@

$(HEIRLOOM_PKGTOOLS)-clean:
	rm -rf $(HEIRLOOM_PKGTOOLS_BUILD_DIR) $(BUILD_HELPER_DIR)/$(HEIRLOOM_PKGTOOLS)*
