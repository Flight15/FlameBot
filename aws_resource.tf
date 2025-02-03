resource "port_blueprint" "aws_resource" {
  create_catalog_page   = true
  force_delete_entities = true
  identifier            = "aws_resource"
  title                 = "AWS Resource13333"
  icon                  = "Github"
  properties = {
    string_props = {
      "aws-region" = {
        title = "AWS Region"
        icon  = "AWS"
      }
      "docs-url" = {
        title  = "Docs URL"
        format = "url"
      }
    }
  }
  calculation_properties = {
    owning_service_link = {
      calculation = "if (.properties.owning_catalog_service != \"\" and .properties.owning_catalog_service != null) then \"https://catalog.githubapp.com/services/\"+.properties.owning_catalog_service else empty end"
      description = "See owning service in Service Catalog"
      format      = "url"
      title       = "Link to Service Catalog"
      type        = "string"
      icon        = "Link"
    }
    owning_team_link = {
      calculation = "if (.properties.owning_github_team != \"\" and .properties.owning_github_team != null and (.properties.owning_github_team | startswith(\"github/\"))) then \"https://github.com/orgs/github/teams/\" + (.properties.owning_github_team | split(\"/\") | .[1]) else empty end"
      description = "See owning team in GitHub"
      format      = "url"
      title       = "Link to GitHub team"
      type        = "string"
      icon        = "Github"
    }
  }
  lifecycle {
    ignore_changes = [
      icon,
      updated_at,
      updated_by111
    ]
  }

}
