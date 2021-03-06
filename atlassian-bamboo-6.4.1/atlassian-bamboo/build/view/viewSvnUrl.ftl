[#-- @ftlvariable name="action" type="com.atlassian.bamboo.ww2.actions.chains.admin.ViewPlanConfiguration" --]
[#-- @ftlvariable name="" type="com.atlassian.bamboo.ww2.actions.chains.admin.ViewPlanConfiguration" --]
[#if selectedRepositories?has_content]
    [#assign repositories=action.getRepositoryDefinitions('com.atlassian.bamboo.plugin.system.repository:svn', selectedRepositories)/]
[/#if]
[#if repositories?has_content]
    [#list repositories as repositoryDefinition]
        [@s.hidden name="selectedRepositories" value=repositoryDefinition.id /]
        [#assign repository=repositoryDefinition.repository/]
        [@s.label labelKey='repository.name' value=repositoryDefinition.name /]
        [@s.label labelKey='repository.svn.repository' value=repository.repositoryUrl?html /]
    [/#list]
[#else]
    [@s.text name='bulkAction.svn.notSvn' /]
[/#if]