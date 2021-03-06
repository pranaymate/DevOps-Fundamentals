[#import "/fragments/decorator/decorators.ftl" as decorators/]
[@decorators.displayHtmlHeader requireResourcesForContext=["atl.general", "bamboo.deployment"] /]
[#include "/fragments/showAdminErrors.ftl"]

${soy.render("bamboo.deployments:deployment-config-layout", "bamboo.layout.deploymentConfig", {
"deploymentProject": deploymentProject,
"content": body,
"showExportToYaml": featureManager.isExportToYamlUiEnabled(),
"showExportToSpecs": featureManager.isExportToJavaSpecsEnabled()
})}

[#include "/fragments/decorator/footer.ftl"]